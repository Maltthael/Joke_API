import requests

def piadas(tipo="heavy_joke"):
    
    if tipo == "light_joke":
        
        url = "https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,explicit"
    else:
        url = "https://v2.jokeapi.dev/joke/Dark?blacklistFlags="

    try:
        answ = requests.get(url)
        if answ.status_code == 200:
            dados = answ.json()
            
        
        if dados["type"] == "twopart":
            return (dados["setup"]), (dados["delivery"])

        elif dados["type"] == "single":
            return(dados["joke"]), None
        
    except Exception as e:
        return f"Erro: {e}", None

    
piadas()



