from ..model import driver_shema
class Driver:
    def __init__(self, driver_num, driver_first_name, driver_last_name, driver_birth_date, driver_team):
        self.driver_num = driver_num
        self.driver_first_name = driver_first_name
        self.driver_last_name = driver_last_name
        self.driver_birth_date = driver_birth_date
        self.driver_team = driver_team

    """This method will create the driver into the database
    """    
    def create_driver(self):
        pass  

    """This method will update a driver on the database
    """
    def update_driver(self):
        pass

    """This method will delete a driver on the database
    """
    def delete_driver(self):
        pass
    
    
    