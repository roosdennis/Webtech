from werkzeug.security import generate_password_hash, check_password_hash




hashed_pass = generate_password_hash("test")

print(hashed_pass)

check = check_password_hash(hashed_pass,'test')
print(check)