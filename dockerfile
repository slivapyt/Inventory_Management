FROM python:3.12.7-slim

WORKDIR /Inventory_Management

ENV PYTHONPATH="${PYTHONPATH}:/Inventory_Management" \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

ENV PIP_ROOT_USER_ACTION=ignore

COPY requirements/dev.txt requirements/prod.txt ./requirements/

RUN apt-get update && \
    apt-get install -y \
    libpq-dev \
    gcc \
    git \
    nodejs \
    curl \
    zsh && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip && \
    pip install -r requirements/dev.txt

RUN git config --global user.name "slivapyt" && \
    git config --global user.email "faer2325@gmail.com"

RUN chsh -s $(which zsh) && \
    sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended && \
    curl -sS https://starship.rs/install.sh | sh -s -- --yes && \
    echo 'eval "$(starship init zsh)"' >> ~/.zshrc

RUN mkdir -p /root/.config && \
    echo '[character]\n\
    success_symbol = "[➜](bold green)"\n\
    error_symbol = "[✖︎](bold red)"\n\
    \n\
    [nodejs]\n\
    disabled = true\n\
    \n\
    [python]\n\
    disabled = true' > /root/.config/starship.toml

COPY .ssh/ /root/.ssh/
RUN chmod 700 /root/.ssh && \
    chmod 600 /root/.ssh/*

COPY . .

EXPOSE 8000
