# Tracking mínimo — Método Black

## O que foi instrumentado
- Captura de `utm_source`, `utm_medium`, `utm_campaign`, `utm_content`, `utm_term`, `ref` e `src`.
- Geração de `session_id` local no navegador.
- Registro local de:
  - pageviews;
  - cliques em checkout;
  - cliques em preview do PDF;
  - visitas na `thanks.html`;
  - conversões locais.
- Propagação automática dos parâmetros de origem para:
  - links de checkout;
  - preview do PDF;
  - página de obrigado;
  - download final do PDF.

## Onde olhar rápido
No console do navegador:

```js
localStorage.getItem('metodo_black_tracking_v1')
localStorage.getItem('metodo_black_tracking_events_v1')
```

## Leitura prática
Isso não substitui analytics centralizado, mas já resolve o principal agora:
- saber de onde veio a visita;
- diferenciar clique de checkout vs. visita na página de entrega;
- manter contexto de origem ao longo do funil.

## Próximo upgrade recomendado
Quando quiser sair do modo mínimo, adicionar um analytics centralizado leve (Plausible, Umami, GoatCounter ou endpoint próprio) para consolidar métricas entre dispositivos/sessões.

## Exemplos de URLs com UTM
### X
```text
https://darussiabillionteam-wq.github.io/metodo-black-openclaw/?utm_source=x&utm_medium=social&utm_campaign=lancamento&utm_content=thread1
```

### Telegram
```text
https://darussiabillionteam-wq.github.io/metodo-black-openclaw/?utm_source=telegram&utm_medium=community&utm_campaign=lancamento&utm_content=grupo_metodosblackbr
```

### Teste manual direto
```text
https://darussiabillionteam-wq.github.io/metodo-black-openclaw/?utm_source=teste&utm_medium=manual&utm_campaign=tracking_minimo
```
