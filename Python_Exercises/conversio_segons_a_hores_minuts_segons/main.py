n=input("Digues un temps en segons")
def update_arrivals(n):
    h = n // 3600
    m = (n % 3600) // 60
    d = n
    return (h, m, n)