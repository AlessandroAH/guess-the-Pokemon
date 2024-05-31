# Guess the Pokemon

Questo progetto è un gioco interattivo chiamato "Guess the Pokemon" in cui i giocatori devono indovinare il nome di un Pokemon basandosi su una foto.

## Funzionalità

- Il gioco mostra un'immagine parziale di un Pokemon e fornisce una serie di indizi per aiutare il giocatore a indovinare il nome corretto.
- I giocatori possono inserire il loro tentativo di risposta e ricevere un feedback immediato sulla correttezza della risposta.
- Il punteggio dei giocatori viene registrato e visualizzato alla fine del gioco.

## Requisiti di sistema

- Python 3.7 o versione successiva
- Libreria grafica pygame
- Flutter SDK

## Istruzioni per l'installazione

1. Clonare o scaricare la cartella "Guess the Pokemon" sul proprio computer.

2. Assicurarsi di avere Python 3.7 o una versione successiva installata sul proprio sistema.

3. Installare Flutter SDK seguendo le istruzioni fornite [qui](https://docs.flutter.dev/get-started/install) per scaricare e installare Flutter SDK sul tuo sistema.

## Istruzioni per l'esecuzione

1. Modificare l'indirizzo IP nel file client `flutter api_service.dart` e nel file server `main.py`.
2. Aprire il terminale o la finestra del prompt dei comandi.
3. Navigare nella cartella "Guess the Pokemon".
4. Eseguire il seguente comando per avviare il gioco:

    ```shell
    python guess_the_pokemon.py
    ```

5. Per eseguire l'applicazione client, navigare nella cartella `client/guess_pokemon` e eseguire il comando:

    ```shell
    flutter run
    ```

6. Per eseguire il server, navigare nella cartella `server` e seguire le istruzioni nel [README](server/README.md) di quella cartella.