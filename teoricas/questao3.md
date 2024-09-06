O resultado é 77.

O código o é seguinte:
```bash
int INDICE = 12, SOMA = 0, K = 1;
while (K < INDICE) {
    K = K + 1;
    SOMA = SOMA + K;
}
print(SOMA);
```

Inicia com K=1 e Soma=0.
Na primeira iteração K vira 2 e soma vira 2.
Na segunda iteração K vira 3 e soma vira 5.
...
Até K virar 12, onde vai encerrar a iteração e SOMA vai estar com o valor 11+10+9+8+7+6+5+4+3+2=1 = 