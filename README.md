# Pincode Information App

This is a simple Flask web application that allows users to fetch details of an Indian pincode using an external API. It also maintains logs of requests and provides basic pages like API documentation, about, and contact.

## Features

- Fetch details of a pincode using an external API.
- View logs of pincode requests.
- API endpoint for programmatic access to pincode details.
- Basic pages like Home, About, Contact, and API Docs.
- Ability to clear request logs.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/shinchain102/Indian-pincodes.git
   cd pincode-app
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:

   ```bash
   python app.py
   ```

4. Open the browser and visit:

   ```
   http://127.0.0.1:5000/
   ```

## API Endpoint

### Fetch Pincode Details

```
GET /api/pincode/<pincode>
```

- **Request Example:**

  ```
  GET http://127.0.0.1:5000/api/pincode/110001
  ```

- **Response Example:**

  ```json
  {
    "status": "success",
    "pincode": "110001",
    "details": [
      {
        "Name": "Connaught Place",
        "District": "Central Delhi",
        "State": "Delhi"
      }
    ]
  }
  ```

## Pages

- **Home ("/")**: Enter a pincode and fetch details.
- **Logs ("/logs")**: View the history of pincode requests.
- **API Docs ("/api-docs")**: Provides API documentation.
- **About ("/about")**: General information about the app.
- **Contact ("/contact")**: Contact form for user inquiries.

## Clearing Logs

- Navigate to `/logs`
- Click the **Clear Logs** button to remove all logs.

## Dependencies

- Flask
- Requests

## License

This project is licensed under the MIT License.

---

Happy Coding! 🚀

