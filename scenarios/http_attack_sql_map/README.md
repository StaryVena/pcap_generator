#sqlmap
Information obtained from: [project homepage](http://sqlmap.org/)

## Introduction
sqlmap is an open source penetration testing tool that automates the process of detecting and exploiting SQL injection flaws and taking over of database servers. It comes with a powerful detection engine, many niche features for the ultimate penetration tester and a broad range of switches lasting from database fingerprinting, over data fetching from the database, to accessing the underlying file system and executing commands on the operating system via out-of-band connections.

## Features
- Full support for MySQL, Oracle, PostgreSQL, Microsoft SQL Server, Microsoft Access, IBM DB2, SQLite, Firebird, Sybase, SAP MaxDB, Informix, HSQLDB and H2 database management systems.
- Full support for six SQL injection techniques: boolean-based blind, time-based blind, error-based, UNION query-based, stacked queries and out-of-band.
- Support to directly connect to the database without passing via a SQL injection, by providing DBMS credentials, IP address, port and database name.
- Support to enumerate users, password hashes, privileges, roles, databases, tables and columns.
- Automatic recognition of password hash formats and support for cracking them using a dictionary-based attack.
- Support to dump database tables entirely, a range of entries or specific columns as per user's choice. The user can also choose to dump only a range of characters from each column's entry.
- Support to search for specific database names, specific tables across all databases or specific columns across all databases' tables. This is useful, for instance, to identify tables containing custom application credentials where relevant columns' names contain string like name and pass.
- Support to download and upload any file from the database server underlying file system when the database software is MySQL, PostgreSQL or Microsoft SQL Server.
- Support to execute arbitrary commands and retrieve their standard output on the database server underlying operating system when the database software is MySQL, PostgreSQL or Microsoft SQL Server.
- Support to establish an out-of-band stateful TCP connection between the attacker machine and the database server underlying operating system. This channel can be an interactive command prompt, a Meterpreter session or a graphical user interface (VNC) session as per user's choice.
- Support for database process' user privilege escalation via Metasploit's Meterpreter getsystem command.
- Refer to the [wiki](https://github.com/sqlmapproject/sqlmap/wiki/Features) for an exhaustive breakdown of the features.


## Documentation
- sqlmap [User's manual](https://github.com/sqlmapproject/sqlmap/wiki).
- sqlmap [History](https://github.com/sqlmapproject/sqlmap/wiki/Historyhttps://github.com/sqlmapproject/sqlmap/wiki/History).
- sqlmap [Frequently Asked Questions (FAQ)](https://github.com/sqlmapproject/sqlmap/wiki/FAQ).
- [Material](https://github.com/sqlmapproject/sqlmap/wiki/Presentations) around sqlmap presented at conferences.

## License
Copyright © 2006-2019 by Bernardo Damele Assumpcao Guimaraes and Miroslav Stampar. All rights reserved.

This program is free software; you may redistribute and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; Version 2 (or later) with the clarifications and exceptions described in the license file. This guarantees your right to use, modify, and redistribute this software under certain conditions. If you wish to embed sqlmap technology into proprietary software, we sell alternative licenses (contact sales@sqlmap.org).

## Disclaimer
This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License v2.0 for more details at http://www.gnu.org/licenses/gpl-2.0.html.

Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program.