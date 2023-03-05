import pathlib
from git import Repo
import sys


class Sync:
    """Class used to automatically sync git repo"""

    def __init__(self) -> None:
        current_path = pathlib.Path(__file__).parent.resolve()
        self.repo = Repo(str(current_path.parent))

    def pull_changes(self):
        """Pull latest changes from repo"""
        self.repo.remotes.origin.pull()

    def get_list_of_changed_files(self) -> list:
        """Get list of changd files"""
        changed = [item.a_path for item in self.repo.index.diff("HEAD")]
        return changed

    def add_all_files_in_repo(self) -> None:
        """Adds files to repo"""
        self.repo.git.add(all=True)

    def commit_changes(self) -> None:
        """Commit all changes"""
        commit_message = self._create_commit_message()
        self.repo.index.commit(commit_message)

    def _create_commit_message(self):
        files_changed = " ".join(self.get_list_of_changed_files())
        message = f"Files changed: {files_changed}"
        return message

    def push_changes(self):
        """Push all changes to first origin"""
        origin = self.repo.remotes[0]
        origin.push()


if __name__ == "__main__":
    sync = Sync()
    number_of_changed_files = len(sync.get_list_of_changed_files())

    if number_of_changed_files == 0:
        sync.pull_changes()

    sync.add_all_files_in_repo()

    if number_of_changed_files > 0:
        sync.commit_changes()
        sync.push_changes()
