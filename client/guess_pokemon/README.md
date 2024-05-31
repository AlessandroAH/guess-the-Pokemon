# Client - Guess Pokemon

Questa è la cartella del client per l'applicazione Guess Pokemon. L'applicazione è scritta in Flutter e può essere eseguita su diverse piattaforme, tra cui iOS, Android, web e Windows.

## Struttura della cartella

La cartella contiene il codice sorgente dell'applicazione, i file di configurazione e le risorse necessarie per eseguire l'applicazione su diverse piattaforme.

- `lib/`: Contiene il codice sorgente dell'applicazione Flutter.
- `ios/`, `android/`, `web/`, `windows/`, `linux/`, `macos/`: Contengono i file di configurazione specifici della piattaforma per eseguire l'applicazione su iOS, Android, web, Windows, Linux e MacOS, rispettivamente.
- `test/`: Contiene i test dell'applicazione.
- `pubspec.yaml`: Il file di configurazione del progetto Flutter, che include le dipendenze del progetto.

## Come eseguire l'applicazione

Per eseguire l'applicazione, assicurati di avere installato Flutter e Dart sul tuo sistema. Poi, naviga nella cartella `guess_pokemon` e esegui il comando:

```sh
flutter run
```

## Installazione l'applicazione sul telefono

### Android

1. Assicurati di avere installato Flutter e Dart sul tuo sistema.
2. Naviga nella cartella `guess_pokemon` e costruisci l'APK con il comando:
```sh
flutter build apk
```
3. Questo creerà un file APK nella cartella build/app/outputs/flutter-apk/.
4. Collega il tuo dispositivo Android al tuo computer.
5. Copia il file APK sul tuo dispositivo e poi installalo utilizzando un file manager.

## Installazione l'applicazione di debug sul telefono

### Android
## Installazione dell'applicazione di debug sul telefono

### Android

1. Assicurati di avere installato Flutter e Dart sul tuo sistema.
2. Collega il tuo dispositivo Android al tuo computer.
3. Abilita le opzioni per sviluppatori sul tuo dispositivo Android e assicurati che il debug USB sia abilitato.
4. Naviga nella cartella `guess_pokemon` e esegui il comando:

```sh
flutter run
```

## iOS
1. Assicurati di avere installato Flutter, Dart e Xcode sul tuo sistema.
2. Collega il tuo dispositivo iOS al tuo Mac.
3. Apri Xcode e vai a "Window" > "Devices and Simulators".
4. Seleziona il tuo dispositivo e assicurati che sia fidato dal tuo Mac.
5. Naviga nella cartella guess_pokemon e esegui il comando:
```sh
flutter run
```
