import sys

# 1. Base de Conhecimento Simulada (O "R" do RAG - Retrieval)
# Num cenário real, isso viria de um Vector Database ou API de E-commerce
estoque = {
    "notebook gamer": "Notebook Gamer X: RTX 3060, i7 12th, 16GB RAM. Preço: R$ 6.500. Ótimo para renderização e jogos pesados.",
    "mouse sem fio": "Mouse Logitech MX Master 3: Ergonômico, bateria de 70 dias. Preço: R$ 600. Ideal para produtividade.",
    "monitor 4k": "Monitor Dell UltraSharp 27'': 4K USB-C. Preço: R$ 3.200. Perfeito para designers e edição de vídeo.",
    "teclado mecânico": "Teclado Keychron K2: Switch Brown, retroiluminado. Preço: R$ 800. Compacto e tátil."
}

def recuperar_contexto(pergunta):
    """
    Simula a busca semântica. Procura palavras-chave da pergunta no estoque.
    """
    print(f"\n[SISTEMA] Buscando no catálogo por termos na pergunta: '{pergunta}'...")
    infos_relevantes = []
    
    for produto, detalhes in estoque.items():
        if any(palavra in pergunta.lower() for palavra in produto.split()):
            infos_relevantes.append(detalhes)
            
    if not infos_relevantes:
        return None
    return "\n".join(infos_relevantes)

def gerar_resposta(pergunta, contexto):
    """
    Simula a geração de resposta do LLM (Como o GPT faria).
    Usa Prompt Engineering para instruir o comportamento.
    """
    if not contexto:
        return "Desculpe, não encontrei esse item específico no nosso estoque atual. Posso ajudar com outra coisa?"
    
    # Prompt do Sistema (System Prompt)
    resposta_simulada = f"""
    🤖 RESPOSTA DO AGENTE:
    Olá! Com base na sua busca, encontrei estas opções incríveis:
    
    {contexto}
    
    Deseja adicionar algum desses ao carrinho ou quer saber mais detalhes?
    """
    return resposta_simulada

def main():
    print("--- 🛒 Smart Shop Assistant (Protótipo RAG) ---")
    print("Digite o que você procura (ex: 'tem notebook gamer?' ou 'preciso de um mouse')")
    print("Digite 'sair' para encerrar.\n")
    
    while True:
        user_input = input("Você: ")
        if user_input.lower() in ['sair', 'exit']:
            break
            
        # Etapa 1: Retrieval (Recuperação)
        contexto = recuperar_contexto(user_input)
        
        # Etapa 2: Generation (Geração Aumentada)
        resposta = gerar_resposta(user_input, contexto)
        
        print(resposta)
        print("-" * 50)

if __name__ == "__main__":
    main()