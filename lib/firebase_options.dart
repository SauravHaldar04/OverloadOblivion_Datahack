// File generated by FlutterFire CLI.
// ignore_for_file: type=lint
import 'package:firebase_core/firebase_core.dart' show FirebaseOptions;
import 'package:flutter/foundation.dart'
    show defaultTargetPlatform, kIsWeb, TargetPlatform;

/// Default [FirebaseOptions] for use with your Firebase apps.
///
/// Example:
/// ```dart
/// import 'firebase_options.dart';
/// // ...
/// await Firebase.initializeApp(
///   options: DefaultFirebaseOptions.currentPlatform,
/// );
/// ```
class DefaultFirebaseOptions {
  static FirebaseOptions get currentPlatform {
    if (kIsWeb) {
      return web;
    }
    switch (defaultTargetPlatform) {
      case TargetPlatform.android:
        return android;
      case TargetPlatform.iOS:
        return ios;
      case TargetPlatform.macOS:
        throw UnsupportedError(
          'DefaultFirebaseOptions have not been configured for macos - '
          'you can reconfigure this by running the FlutterFire CLI again.',
        );
      case TargetPlatform.windows:
        throw UnsupportedError(
          'DefaultFirebaseOptions have not been configured for windows - '
          'you can reconfigure this by running the FlutterFire CLI again.',
        );
      case TargetPlatform.linux:
        throw UnsupportedError(
          'DefaultFirebaseOptions have not been configured for linux - '
          'you can reconfigure this by running the FlutterFire CLI again.',
        );
      default:
        throw UnsupportedError(
          'DefaultFirebaseOptions are not supported for this platform.',
        );
    }
  }

  static const FirebaseOptions web = FirebaseOptions(
    apiKey: 'AIzaSyCTs4G8WgyE92NJrHrUts7lMJFFOXPjW64',
    appId: '1:447052592316:web:58beffaff3879329b28cb9',
    messagingSenderId: '447052592316',
    projectId: 'datahack3-e90e1',
    authDomain: 'datahack3-e90e1.firebaseapp.com',
    storageBucket: 'datahack3-e90e1.appspot.com',
  );

  static const FirebaseOptions android = FirebaseOptions(
    apiKey: 'AIzaSyCHVTgPiLzY3YeWDBPdlg3ZGTjxHKpXEMw',
    appId: '1:447052592316:android:f3512a2c04d56fbcb28cb9',
    messagingSenderId: '447052592316',
    projectId: 'datahack3-e90e1',
    storageBucket: 'datahack3-e90e1.appspot.com',
  );

  static const FirebaseOptions ios = FirebaseOptions(
    apiKey: 'AIzaSyBFSZFFrYyBo_S3oXlXkxNSNg1IA0-XzYY',
    appId: '1:447052592316:ios:b09bc116331b3f41b28cb9',
    messagingSenderId: '447052592316',
    projectId: 'datahack3-e90e1',
    storageBucket: 'datahack3-e90e1.appspot.com',
    iosBundleId: 'com.example.datahack',
  );
}