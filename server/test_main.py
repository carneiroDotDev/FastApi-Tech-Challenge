from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

filename_formatted = "size-distribution1.csv"
csv_formatted = f"./assets/{filename_formatted}"
file_formated = {'file': (csv_formatted, open(
    csv_formatted, 'rb'), 'text/csv')}

filename_broken = "broken-distribution.csv"
csv_broken = f"./assets/{filename_broken}"
file_broken = {'file': (csv_broken, open(csv_broken, 'rb'), 'text/csv')}

filename_wrong_extension = "broken-distribution"
csv_wrong_extension = f"./assets/{filename_wrong_extension}"
file_wrong_extension = {
    'file': (csv_wrong_extension, open(csv_wrong_extension, 'rb'), 'text/csv')}


def test_root_route():
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers['content-type']
    assert """<input name="file" type="file" required>""" in response.text


def test_findmax_route():
    with open(csv_formatted, 'rb') as f:
        response = client.post("/findmax/", files=file_formated)
        print, response
        assert response.status_code == 200
        assert "application/json" in response.headers['content-type']
        assert "53.3669" in response.text
        assert "0.08432081" in response.text

    with open(csv_broken, 'rb'):
        response = client.post("/findmax/", files=file_broken)
        print, response
        assert response.status_code == 400
        assert "application/json" in response.headers['content-type']
        assert "Bad file format. Considered .csv with ; as separator and two columns (Radius and Frequency)." in response.text

    with open(csv_wrong_extension, 'rb'):
        response = client.post("/findmax/", files=file_wrong_extension)
        print, response
        assert response.status_code == 411
        assert "application/json" in response.headers['content-type']
        assert "File extension is not .csv" in response.text
