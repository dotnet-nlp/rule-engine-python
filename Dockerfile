FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=UTC

# some tools
RUN apt-get update \
 && apt-get install -y software-properties-common \
 && apt-get install -y wget \
 && apt-get install -y unzip \
 && apt-get install -y apt-transport-https \
 && apt-get install -y gnupg \
 && apt-get install -y ca-certificates \
 && apt-get install -y build-essential

# install mono
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF \
 && echo "deb https://download.mono-project.com/repo/ubuntu stable-focal main" | tee /etc/apt/sources.list.d/mono-official-stable.list \
 && apt-get update \
 && apt-get install -y mono-devel=6.12\*

# install python and pip
RUN apt-get update \
 && add-apt-repository ppa:deadsnakes/ppa \
 && apt-get update \
 && apt-get install -y python3.8-full python3.8-dev \
 && wget https://bootstrap.pypa.io/get-pip.py \
 && python3.8 get-pip.py \
 && rm get-pip.py \
 && rm -rf /var/lib/apt/lists/*

# install pythonnet
RUN pip install --upgrade pip \
 && pip install --upgrade setuptools \
 && pip install --upgrade scons \
 && pip install --upgrade wheel \
 && pip install --upgrade pythonnet==2.5.2

# clone repository
RUN cd /opt \
 && wget https://github.com/dotnet-nlp/rule-engine/archive/refs/heads/main.zip \
 && unzip main.zip \
 && rm main.zip

# install dotnet
#RUN wget https://packages.microsoft.com/config/ubuntu/20.04/packages-microsoft-prod.deb \
# && dpkg -i packages-microsoft-prod.deb \
# && rm packages-microsoft-prod.deb \
# && apt-get update \
# && apt-get install -y dotnet-sdk-6.0

# publish dlls
#RUN cd /opt/rule-engine-main \
# && dotnet publish RuleEngine.Core/RuleEngine.Core.csproj -p:RuntimeIdentifier=linux-x64 -c Release --self-contained --output /opt/release \
# && dotnet publish RuleEngine.Mechanics.Peg/RuleEngine.Mechanics.Peg.csproj -p:RuntimeIdentifier=linux-x64 -c Release --self-contained --output /opt/release \
# && dotnet publish RuleEngine.Mechanics.Regex/RuleEngine.Mechanics.Regex.csproj -p:RuntimeIdentifier=linux-x64 -c Release --self-contained --output /opt/release

RUN rm -rf /var/lib/apt/lists/* \
 && rm -rf /tmp/*

COPY test.py /opt/
