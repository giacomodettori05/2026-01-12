from database.DB_connect import DBConnect
from model.collegamento import Collegamento


class DAO():

    @staticmethod
    def getAllYears():
        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query = "SELECT distinct year FROM seasons s  ORDER BY year"

        cursor.execute(query)

        for row in cursor:
            results.append(row["year"])

        cursor.close()
        conn.close()
        return results

    @staticmethod
    def getAllConstructors(year1, year2):
        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT DISTINCT re.constructorId, re.driverId
                    FROM results re
                    INNER JOIN races r ON re.raceId = r.raceId
                    WHERE re.statusId != 2
                    AND r.year >= %s 
                    AND r.year <= %s """

        cursor.execute(query, (year1, year2))

        for row in cursor:
            results.append(Collegamento( constructorId= row["constructorId"], driverId= row["driverId"]))

        cursor.close()
        conn.close()
        return results

