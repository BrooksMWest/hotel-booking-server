# Update an existing artist

## Description
This ticket requests the implementation of a route that allows updating an existing artist.

## Request
- **Method:** PUT
- **Path:** /artists/{artistId}
- **Body**
  ```json
  {
    "name": "Updated Artist Name",
    "age": 30,
    "bio": "Updated Artist Bio"
  }
  ```

## Response
- **Body**
  ```json
  {
    "id": {artistId},
    "name": "Updated Artist Name",
    "age": 30,
    "bio": "Updated Artist Bio"
  }
  ```
- **Status Code:** 200 OK
