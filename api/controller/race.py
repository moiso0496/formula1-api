from api.model.data_type.session_prefix import prefix

class Result:
    def __init__(self, race_id, result_collection) -> None:
        self.race_id = race_id
        self.result_collection = result_collection

    def _race_on_db(self, race_id):
        result = self.result_collection.get_document({"race_id": race_id})
        return result
    
    def _get_session_prefix(session_id):
        if session_id in prefix:
            return prefix[session_id]

    def _session_on_db(self, race, session_race_prefix, session_id):
        if session_id in race[session_race_prefix]:
            return race[session_race_prefix]
        return None
    
    def manage_race(self, race_id, result_payload):
        race_on_db = self._race_on_db(race_id)
        session_race_prefix = self._get_session_prefix(result_payload["session_id"])
        if race_on_db:
            self.result_collection.update_document({"race_id": race_id}, {session_race_prefix: result_payload})
            if self._session_on_db(race_on_db, session_race_prefix, result_payload["session_id"]):
                return f"Successfully updated  {result_payload['session_id']} on {race_id}"
            else:
                return f"Successfully added  {result_payload['session_id']} on {race_id}"
        else:
            pass
