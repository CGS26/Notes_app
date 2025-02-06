import unittest
from unittest.mock import AsyncMock, patch, MagicMock
from sqlalchemy.orm import Session
from models.model import Note
from dao.note_dao import NoteDAO


class TestNoteDAO(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        """Set up a mock session and NoteDAO instance for testing."""
        self.mock_db = AsyncMock(spec=Session)
        self.mock_db.execute = AsyncMock()
        self.mock_db.commit = AsyncMock()
        self.mock_db.refresh = AsyncMock()
        self.mock_db.delete = AsyncMock()  #
        self.note_dao = NoteDAO(db=self.mock_db)

    @patch("dao.note_dao.select")
    async def test_get_note_by_id_found(self, mock_select):
        """Test retrieving a note by ID when it exists."""
        mock_note = Note(note_id=123, title="Test", body="Body", user_id=1)
        mock_result = AsyncMock()
        mock_result.scalars.return_value.first.return_value = mock_note 
        self.mock_db.execute.return_value = mock_result

        result = await self.note_dao.get_note_by_id(123)

        self.mock_db.execute.assert_called_once()
        self.assertEqual(result.note_id, 123)

    @patch("dao.note_dao.select")
    async def test_get_note_by_id_not_found(self, mock_select):
        """Test retrieving a note by ID when it doesn't exist."""
        mock_result = AsyncMock()
        mock_result.scalars.return_value.first.return_value = None
        self.mock_db.execute.return_value = mock_result

        result = await self.note_dao.get_note_by_id(123)

        self.assertIsNone(result)

    @patch("dao.note_dao.NoteDAO.get_note_by_id")
    async def test_delete_note_success(self, mock_get_note_by_id):
        """Test deleting a note successfully."""
        mock_note = Note(note_id=123, title="Test Note", body="Test Body", user_id=1)
        mock_get_note_by_id.return_value = mock_note

        result = await self.note_dao.delete_note(123)

        self.mock_db.delete.assert_called_once_with(mock_note)
        self.mock_db.commit.assert_called_once()
        self.assertEqual(result.note_id, 123)



if __name__ == "__main__":
    unittest.main()
