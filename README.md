Product classifier

This script was made during the selection process of the company Birdie, in July 2019.

It takes a list of various products and classifies each one as Smartphone related or Non-smartphone related, based on pre-defined keywords like "smartphone".

Some considerations and acknowledgement of a few possible problems present in the code:
- Python is not one of my most familiar languages.
- At first, I thought about using a Naive Bayes classifier, but using probability seemed overkill for this application, and also would require a testing set with known results, so I thought a more straightforward solution would be better.

- Possible problem at line 19: All keywords were chosen by me, after a quick scan of the product names and popular smartphone brands. Maybe some automated process for defining keywords would make the results better.
- Possible problem at line 27: I tried to remove accents and special characters (like "ã" to "a", "ç" to "c" and "ô" to "o"). Through some searching, I found these unicode functions, but the end result was not quite as expected. There probably is a better solution that I haven't found.
- Possible problem at line 34: I want to check if there is an intersection between the keyword array and the current product's tokens. I found a solution of putting both arrays into sets, and the & operator to return true if there is intersection. It worked fine, but I don't actually know if this is best on performance and memory allocation.

EM PORTUGUÊS:

Classificador de produtos

Esse script foi feito durante o processo seletivo da empresa Birdie, em Julho de 2019.

Ele tem como entrada uma lista de vários produtos e classifica cada um como relacionado ou não a Smartphones, baseado em keywords pré-definidas, como "smartphone".

Algumas considerações e reconhecimento de possíveis problemas presentes no código:
- Python não é uma das minhas línguas mais familiares.
- Inicialmente, eu pensei em usar um classificador Naive BAyes, mas usar probabilidade pareceu overkill para esse problema, e tambem exigiria um conjunto de testes com resultados conhecidos, então achei que uma solução mais simples e direta seria melhor.

- Possivel problema na linha 19: Todas as keywords foram escolhidas por mim, após uma análise rápida dos nomes de produtos e de marcas populares de smartphones. Talvez um processo automático para definir keywords tornasse os resultados melhores.
- Possível problema na linha 27: Eu tentei remover acentos e caracteres especiais (como "ã" vira "a", "ç" vira "c" e "ô" vira "o"). Após pesquisar, eu achei essas funções de unicode, mas o resultado final não foi como esperado. Talvez haja uma solução melhor que eu não achei.
- Possível problema na linha 34: Eu quis checar se há interceção entre o vetor de keywords e os tokens do produto atual. Eu achei essa solução de colocar os dois vetores em sets e usar o operador & para retornar true se houver interseção. Funcionou bem, porém não sei se é a melhor solução pensando em performance e alocação de memória.