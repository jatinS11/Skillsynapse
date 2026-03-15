import urllib.request, json
req = urllib.request.Request('http://localhost:3000/api/chat', data=json.dumps({'message': 'What is a full stack developer?'}).encode(), headers={'Content-Type': 'application/json'}, method='POST')
try:
    resp = urllib.request.urlopen(req, timeout=30)
    data = json.loads(resp.read())
    print(f"Success!")
    print(f"Source: {data.get('source')}")
    print(f"Reply length: {len(data.get('reply', ''))}")
    print(f"Preview: {data.get('reply', '')[:200]}")
except Exception as e:
    print(f"Error Type: {type(e)}")
    print(f"Error message: {e}")
    print(f"Error status code: {getattr(e, 'code', 'Unknown')}")
    if hasattr(e, 'read'):
        try:
            body = e.read()
            print(f"Raw body bytes: {body}")
            print(f"Response: {body.decode('utf-8', errors='ignore')}")
        except Exception as inner_e:
            print(f"Could not read response: {inner_e}")
