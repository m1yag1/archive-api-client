from archive_client.models import ClientCore, Collection


class ArchiveClient(ClientCore):
    def __init__(self, session=None, root_url=None):
        super(ArchiveClient, self).__init__({}, session or self.new_session())
        if root_url:
            self.session.root_url = root_url

    def get_collection(self, cnx_id):
        url = self.session.build_url("contents", f"{cnx_id}.json")

        response = self.get(url)
        return Collection(response.json(), session=self.session)
