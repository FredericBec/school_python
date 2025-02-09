from typing import Optional

from daos.dao import Dao
from models.address import Address


class AddressDao(Dao[Address]):
    def create(self, address: Address) -> int:
        id_address = 0
        return id_address

    def read(self, id_address: int) -> Optional[Address]:
        """
        Retrieve an optional address in database
        :param id_address: id
        :return: address
        """
        address: Optional[Address]
        with Dao.connection.cursor() as cursor:
            sql = "SELECT * FROM address WHERE id_address = %s"
            cursor.execute(sql, (id_address,))
            record = cursor.fetchone()
        if record is not None:
            address = Address(record['street'], record['city'], record['postal_code'])
            address.id = record['id_address']
        else:
            address = None
        return address

    def update(self, address: Address) -> bool:
        return False

    def delete(self, address: Address) -> bool:
        return False

    def read_all(self) -> list[Address]:
        address_list: list[Address] = []
        return address_list
