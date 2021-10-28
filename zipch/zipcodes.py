import csv
import dataclasses
import os
import tempfile
import zipfile
from urllib.request import urlretrieve


@dataclasses.dataclass
class Location:
    official_name: str
    canton: str
    municipality: str


class ZipcodesDatabase:
    """
    Database of swiss zipcodes.

    The main methods are :meth:`get_zipcodes_list` and :meth:`get_zipcode`,
    that will download the zipcodes database if necessary, parse it and return
    a `Location` instance.

    Use it like this:

        >>> zd = ZipcodesDatabase('/tmp/zipcodes')
        >>> zd.get_location(1003)
        Location(official_name='Lausanne', canton='VD', municipality='Lausanne')

    The CSV file has the following fields, in this order:

    Ortschaftsname   nom officiel de la localité
    PLZ              code postal (NPA) à quatre chiffres,
                     compris entre 1000 et 9999
    Zusatzziffer     La valeur des chiffres supplémentaires est comprise entre
                     0 et 99. Combinés à l'attribut PLZ, ils donnent
                     naissance au NPA6.
    Gemeindename     nom de la commune principale de la localité
    BFS-Nr           numéro de la commune principale de la localité
    Kantonskürzel    abréviation du canton dans lequel la localité se trouve
                     majoritairement
    E                la coordonnée Est indique la position d’un point
                     quelconque au sein du périmètre de la localité ou du code
                     postal.
    N                la coordonnée Nord indique la position d’un point
                     quelconque au sein du périmètre de la localité ou du code
                     postal.
    """

    DOWNLOAD_URL = "http://data.geo.admin.ch/ch.swisstopo-vd.ortschaftenverzeichnis_plz/PLZO_CSV_LV95.zip"  # NOQA

    def __init__(self, file_path):
        """
        ``file_path`` is the path to the CSV file containing the zipcodes. You
        can put an inexistent file here, in which case the file will be
        downloaded from the internets.
        """
        self.file_path = file_path
        self.zipcode_mapping = {}

    def download(self, overwrite=True):
        """
        Download the zipcodes CSV file. If ``overwrite`` is set to False, the
        file won't be downloaded if it already exists.
        """
        if overwrite or not os.path.exists(self.file_path):
            _, f = tempfile.mkstemp()
            try:
                urlretrieve(self.DOWNLOAD_URL, f)
                extract_csv(f, self.file_path)
            finally:
                os.remove(f)

    def get_locations(self):
        """
        Return the zipcodes mapping as a list of ``{zipcode: location}`` dicts.
        The zipcodes file will be downloaded if necessary.
        """
        if self.zipcode_mapping:
            return self.zipcode_mapping

        self.download(overwrite=False)

        zipcode_mapping = {}
        with open(self.file_path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=";")
            # Skip header
            next(csv_reader)
            for line in csv_reader:
                zipcode_mapping[int(line[1])] = Location(
                    official_name=line[0], canton=line[5], municipality=line[3]
                )
        self.zipcode_mapping = zipcode_mapping

        return self.zipcode_mapping

    def get_location(self, zipcode):
        """
        Return the place name of the given zipcode. Raises :class:`IndexError`
        if the zipcode doesn't exist.
        """
        return self.get_locations()[zipcode]

    def get_zipcodes_for_municipality(self, municipality):
        zipcodes = [
            zipcode
            for zipcode, location in self.get_locations().items()
            if location.municipality == municipality
        ]

        return zipcodes

    def get_zipcodes_for_canton(self, canton):
        """
        Return the list of zipcodes for the given canton code.
        """
        zipcodes = [
            zipcode
            for zipcode, location in self.get_locations().items()
            if location.canton == canton
        ]

        return zipcodes

    def get_cantons(self):
        """
        Return the list of unique cantons, sorted by name.
        """
        return sorted(
            list(set([location.canton for location in self.get_locations().values()]))
        )

    def get_municipalities(self):
        """
        Return the list of unique municipalities, sorted by name.
        """
        return sorted(
            list(
                set(
                    [
                        location.municipality
                        for location in self.get_locations().values()
                    ]
                )
            )
        )


def extract_csv(zip_path, destination):
    """
    Extract the first CSV file found in the given ``zip_path`` ZIP file to the
    ``destination`` file. Raises :class:`LookupError` if no CSV file can be
    found in the ZIP.
    """
    with zipfile.ZipFile(zip_path) as zf:
        member_to_unzip = None
        for member in zf.namelist():
            if member.endswith(".csv"):
                member_to_unzip = member
                break

        if not member_to_unzip:
            raise LookupError("Couldn't find any CSV file in the archive")

        with zf.open(member_to_unzip) as zfp, open(destination, "wb") as dfp:
            dfp.write(zfp.read())
