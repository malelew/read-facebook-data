# read-facebook-data FKA: ucbmeft-data
This started out as a look at the Berkley meme FB group membership after the
moderators decided to limit further membership to Cal students and alumni.
The project ran into complications with FB api access permissions but the
read-data.py file is still useful for gathering Facebook data.

The read-data.py execution takes in a CSV with that contains a row of 
Facebook IDs writes to separate CSV the dict object related to the ID.
For any GraphAPI errors the row in the CSV will contain a single F.

Example Execution: "python read-data.py fb-data.csv fb-output.csv"

Before exeucting make sure to include a facebook api access token as detailed
here, https://developers.facebook.com/docs/facebook-login/access-tokens. Also
the FB_ID_COLUMN variable corressponds with the column containing the FB ids.

If you would rather look into other data and relations than you can adjust the
get_object with anything present in the documentation:
http://facebook-sdk.readthedocs.io/en/latest/api.html
