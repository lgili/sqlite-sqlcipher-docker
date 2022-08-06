# About This Image

Easy Encrypt and Decrypt [SQLite](https://www.sqlite.org) databases with [SQLCipher](https://www.zetetic.net/sqlcipher).
Based on [pallocchi/docker](https://github.com/pallocchi/docker).

# How to Use this Image

This image contains 3 utils `csv2sqlite` (convert csv to sqlite), `sqlenc` (encrypt) and `sqldec` (decrypt) that do the hard work for you.

### Convert to sqlite

```bash
docker run -v <workdir>:/sqlcipher lgili/sqlcipher csv2sqlite <csv-file> <db-plain> <table-name>
```

### Encrypt

```bash
docker run -v <workdir>:/sqlcipher lgili/sqlcipher sqlenc <db-plain> <db-encrypted> <PASSPHRASE>
```

### Decrypt

```bash
docker run -v <workdir>:/sqlcipher lgili/sqlcipher sqldec <db-encrypted> <db-plain> <PASSPHRASE>
```
### Parameters

| Name                       | Description                                                                                                                           |
|----------------------------|---------------------------------------------------------------------------------------------------------------------|
| `workdir`                | Local directory where `db-plain` is present and  `db-encrypted` will be created. |
| `csv-file`               | Filename of the csv to convert to sqlite (must be present in `workdir`). 
| `db-plain`               | Filename of the database to encrypt (must be present in `workdir`).                       |
| `db-encrypted`      | Filename of the encrypted database which will be created.                                         |
| `passphrase`         | Passphrase used by SQLCipher to encrypt the database                                              |

## Example

Our database to encrypt is in `./databases`directory.

```bash
$ ls databases
$ file.csv
```
Convert csv file to the sqlite, generating the `my-data.db3` file.

```bash
$ docker run -v ${PWD}/databases:/sqlcipher lgili/sqlcipher csv2sqlite file.csv my-data.db3 table
```
Verify that the new database was created.
```bash
$ ls databases
$ file.csv my-data.db3
```

Encrypt the database, generating the `my-encrypted.db3` file.

```bash
$ docker run -v ${PWD}/databases:/sqlcipher lgili/sqlcipher sqlenc my-data.db3 my-encrypted.db3 password
```

Verify that the new encrypted database was created.

```bash
$ ls databases
$ file.csv my-data.db3 my-encrypted.db3
```

Let's decrypt the previously generated database.

```bash
$ docker run -v ${PWD}/databases:/sqlcipher lgili/sqlcipher sqldec my-encrypted.db3 my-decrypted.db3 password
```

Verify that the new database was created.

```bash
$ ls databases
$ file.csv my-data.db3 my-encrypted.db3 my-decrypted.db
```
# Feedback

Please direct all feedback to [lgili/sqlite-sqlcipher-docker](https://github.com/lgili/sqlite-sqlcipher-docker/issues).



