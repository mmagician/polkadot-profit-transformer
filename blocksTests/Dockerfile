FROM python:3.8


# upgrade pip and install selenium
RUN pip install --upgrade pip
COPY . .
WORKDIR /blocksTests
RUN pip install -r requirements.txt

ENV DISPLAY=:99

ADD blocksTests/data/id_rsa /root/.ssh/id_rsa
RUN chown root:root /root/.ssh/id_rsa
RUN chmod 700 ~/.ssh/id_rsa

COPY . .

ENTRYPOINT [ "./entrypoint.sh" ]
# ENV PATH='./project/tests/suites/rewardLimit.py'
# CMD [ 'python','-u','-m pytest -v ./tests/suites/rewardLimit.py' ]
# CMD [ "/bin/sh", "-c", "python -m pytest -v ./tests/suites/.py 2>&1" ]
