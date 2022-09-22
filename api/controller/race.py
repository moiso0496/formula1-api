from re import search
from api.model.data_type.session_prefix import prefix
from api.model.data_type.data_type import data_types


class Result:
    def __init__(self,result_collection, race_id=None, ) -> None:
        self.race_id = race_id
        self.result_collection = result_collection

    def _race_on_db(self, race_id):
        result = self.result_collection.get_document({"race_id": race_id})
        return result
    
    def _get_session_prefix(self, session_id):
        if session_id in prefix:
            return prefix[session_id]

    def _session_on_db(self, race, session_race_prefix):
        if session_race_prefix in race:
            return race[session_race_prefix]
        return None
    
    def manage_race(self, race_id, result_payload):
        # Determine if the race is on the database
        race_on_db = self._race_on_db(race_id)
        # Get the session id prefix of the race
        session_race_prefix = self._get_session_prefix(result_payload["session_id"])
        #If the race on the databse
        if race_on_db:
            # Find out if the session is on the Database
            session_on_db = self._session_on_db(race_on_db,session_race_prefix)
            # If the session is on the database
            if session_on_db:
                #Append session result to the session id of the race
                session_on_db["session_results"].append(result_payload["session_results"])
                # Update the document of the race
                self.result_collection.update_document({"race_id": race_id}, {session_race_prefix: session_on_db})
                # Return a successful message
                return f"Successfully updated  {result_payload['session_id']} on {race_id}"
            else:
                # If the session does not exits add the first session result for the session id of the race
                self.result_collection.update_document({"race_id": race_id}, {session_race_prefix: [result_payload["session_results"]]})
                return f"Successfully added  {result_payload['session_id']} on {race_id}"
        else:
            # Create a new race dictionary
            new_race = {}
            # Add the race id
            new_race["race_id"] = race_id
            # Add the session  and the session results to the new race
            new_race[session_race_prefix] = {
                "session_id" : result_payload["session_id"],
                "session_results" : [result_payload["session_results"]]
            }
            # Create a new document
            response = self.result_collection.create_document(new_race)
            if response:
                return f'Successfully added race {race_id} on DB, {result_payload["session_id"]} was added.'
    
    def get_races_results(self, race_query=None, filter_query={}):
        result = None
        if not race_query:
            result = self.result_collection.get_all_documents(filter_query)
        else:
            result = self.result_collection.get_one_document_with_filter_values(race_query, filter_query)

        if not result:
            return f'No drivers found'
        return result if type(result) == data_types["Dictionary"] else list(result)      

