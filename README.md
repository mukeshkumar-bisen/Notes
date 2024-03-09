# Notes
Project Description: Simple Note Taking API


http://127.0.0.1:8000/notes/
here add data  or create new note
	title = note1,
	body =  body1

http://127.0.0.1:8000/notes/1/
notes/<pk>/: here Fetch a note by its primary key.
its ability to update the title and body of an existing note identified by its primary key.

http://127.0.0.1:8000/notes/query/?title=n3
Query Notes by Title Substring: Implement functionality to query notes based on a substring present in the note's title, returning all matching notes.
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept
    
        "id": 3,
        "title": "n3",
        "body": "v3",
        "created_at": "2024-03-09T08:20:24.798356Z",
        "updated_at": "2024-03-09T08:20:24.798356Z"

Update Note: Provide the ability to update the title and body of an existing note identified by its primary key.
http://127.0.0.1:8000/notes/1/
update note using title and body field 
