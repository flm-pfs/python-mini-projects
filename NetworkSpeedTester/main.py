import speedtest


def test_network_speed():
    st = speedtest.Speedtest()
    print("Testing network speed...")

    # Get the best server for testing
    st.get_best_server()

    # Perform the download and upload speed tests
    new_var = 1_000_000
    download_speed = st.download() / new_var  # Convert to Mbps
    upload_speed = st.upload() / new_var  # Convert to Mbps

    print(f"Download Speed: {download_speed:.2f} Mbps")
    print(f"Upload Speed: {upload_speed:.2f} Mbps")


if __name__ == "__main__":
    test_network_speed()
