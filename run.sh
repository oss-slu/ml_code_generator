export FN_AUTH_REDIRECT_URI=http://localhost:8040/google/auth
export FN_BASE_URI=http://localhost:8040
export FN_CLIENT_ID=flask_app/env.GOOGLE_CLIENT_ID
export FN_CLIENT_SECRET=flask_app/env.GOOGLE_CLIENT_SECRET

export FLASK_APP=flask_app/api/app.py
export FLASK_DEBUG=1
//export FN_FLASK_SECRET_KEY=SOMETHING RANDOM AND SECRET

python -m flask run -p 8040