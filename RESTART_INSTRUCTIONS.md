# 🔄 Connection Fix Instructions

## The Issue
The "Proxy error" or "Error Occurred" happens because:
1. React (port 3001) is trying to talk to Django via `localhost`
2. Django is listening on `127.0.0.1` (IPv4)
3. Windows sometimes resolves `localhost` to IPv6 (`::1`), causing a mismatch

## ✅ The Fix
I have updated `package.json` to explicitly use `http://127.0.0.1:8000`.

## 🚨 CRITICAL: YOU MUST RESTART REACT

For the changes to take effect, you **MUST** restart the frontend server:

1. Go to your **Web Frontend Terminal** (where `npm start` is running)
2. Press `Ctrl + C` to stop it
3. Type `Y` (if prompted) to confirm
4. Run `npm start` again

## 🧪 Verification

1. Backend Terminal should be running: `python manage.py runserver`
2. Frontend Terminal should be running: `npm start`

**Open http://localhost:3001 and try to login again.**

If you see an error now, it will be SPECIFIC (e.g. "Network Error" or "400 Bad Request").

## Troubleshooting

If it STILL fails:

1. **Stop EVERYTHING** (Close all terminals)
2. Open new terminal for Backend:
   ```bash
   cd backend
   venv\Scripts\activate
   python manage.py runserver 0.0.0.0:8000
   ```
   (Note the `0.0.0.0:8000` - this forces it to listen on all addresses)

3. Open new terminal for Frontend:
   ```bash
   cd web-frontend
   npm start
   ```

4. Try accessing via `http://127.0.0.1:3001` instead of localhost.
