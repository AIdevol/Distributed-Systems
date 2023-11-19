
import requests

def publish_book(book_id):
    try:
        response = requests.post('http://publishing-service:5001/publish_book', json={'book_id': book_id})
        response.raise_for_status()
        return response.json().get('result', 'add_book')
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"
