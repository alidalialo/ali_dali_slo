import socket

cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cs.connect(('127.0.0.1', 12345))
num_questions = int(cs.recv(1024).decode())
for i in range(num_questions):
    question = cs.recv(1024).decode()
    answer = input(f"{question}: ")
    cs.sendall(answer.encode())
final_score = cs.recv(1024).decode()
print(f"results: {final_score}")

