FROM caltechads/earthworm:7.9-build3

ENV PYTHONUNBUFFERED 1

#install packages
RUN yum -y makecache fast && \
    yum update -y && \
    yum install -y \
        git \
        # These python36u packages come from the ius-release repo, which we install above.
        python36u \
        python36u-devel \
        python36u-pip && \
    # Add symlinks for python3.6/pip3.6 to just python3/pip3. These won't be needed under most circumstances, due to the
    # ENV line that we run next. I added them just to stay consistent with other ADS Dockerfiles.
    ln -s /usr/bin/python3.6 /usr/bin/python3 && \
    ln -s /usr/bin/pip3.6 /usr/bin/pip3 && \
    # Create the venv for multitenent's environment to live it.
    python3 -m venv /ve

# Ensure that we run the pip and python that are in the virtualenv, rather than the system copies.
ENV PATH /ve/bin:$PATH

COPY . /app
WORKDIR /app

# Try building python_ew
RUN python3 setup.py build && \
    python3 setup.py install

# Now package it
RUN python setup.py sdist
