FROM		python:3.9

RUN			git clone https://github.com/alvrodri/get_next_line $HOME/infection

COPY		./includes/entrypoint.sh /
RUN			chmod 700 /entrypoint.sh

WORKDIR		/var/app
COPY		./bin/stockholm .
RUN			chmod 700 stockholm

ENTRYPOINT [ "/entrypoint.sh" ]