#! /bin/bash

ls ./pdf | egrep "*.pdf" | xargs -I {} pdftotext -layout pdf/{} txt/{}.txt
