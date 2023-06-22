import socket,threading

questions = {
"Who are real madrid legend? :\na.cr7\nb.messi": "a", "What is the capital of Syria? :\na.Damascus\nb.aleppo": "a", "What is the best department to study? :\na.ECe\nb.medecine": "b", "how many years you have yo study in ece? :\na.4\nb.5": "b", "What is liverpool ? :\na.club\nb.company": "a", "What is the top goal scorrer in world? :\na.messi\nb.ronaldo": "a", "What is the currency of Canada? :\na.Dollar\nb.Euro": "a", "What is the currency of France? :\na.Dollar\nb.Euro": "b", "What is the capital of america? :\na.NY\nb.whashinton": "b", "What is the currency of Russia? :\na.Ruble\nb.Euro": "a", "What is the capital of France? :\na.paris\nb.marssiaile": "a", "What is the currency of Saudi Arabia? :\na.Riyal\nb.Dollar": "a", "What is the capital of lebanon? :\na.tarablus\nb.beirut": "b", "What is the capital of Italy? :\na.roma\nb.milan": "a", "What is the currency of Egypt? :\na.Pound\nb.Dollar": "a", "What is argentina legend? :\na.higuain\nb.messi": "b", "What is the capital of United Kingdom? :\na.london\nb.manchester": "a", "What is the capital of Spain? :\na.madrid\nb.barcelona": "a", "What is the capital of jordan? :\na.amman\nb.irbed": "a", "What is the capital of ksa? :\na.ryiadh\nb.jeddah": "a"}

result = {}

def handle_request(cs, cadd):
    cs.send(str(len(questions)).encode())
    for question in questions:
        cs.send(question.encode())
        client_ans = cs.recv(10).decode().strip()
        if client_ans.upper() == questions[question].upper():
            result[cadd] = result.get(cadd, 0) + 1
    score = result.get(cadd, 0)
    cs.send(f"Score: {score}/{len(questions)}\n".encode())
    cs.close()

class handle_client_thread(threading.Thread):
    def __init__(self,cs,cadd):
        threading.Thread.__init__(self)
        self.cs=cs
        self.cadd=cadd

    def run(self):
        handle_request(self.cs,self.cadd)

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind(('127.0.0.1',12345))
ss.listen(5)
print("i am waiting your answer.")
while True:
    cs, cadd = ss.accept()
    print(f"Connected to {cadd}")
    client = handle_client_thread(cs, cadd)
    client.start()



