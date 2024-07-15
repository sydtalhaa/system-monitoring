# Use an official Ubuntu as the base image
FROM ubuntu:latest

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive

# Install necessary packages
RUN apt-get update --fix-missing && \
    apt-get install -y sudo python3 python3-pip && \
    apt-get install -y stress && \
    apt-get install -y s-tui

# Copy the script to the container
COPY main.py /usr/local/bin/main.py

# Make the script executable
RUN chmod +x /usr/local/bin/main.py

# Run the script
CMD ["python3", "/usr/local/bin/main.py"]

