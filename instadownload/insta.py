import instaloader

# Initialize Instaloader with correct parameters
loader = instaloader.Instaloader(
    download_comments=False,
    save_metadata=False,
    max_connection_attempts=20
)

url = 'https://www.instagram.com/reel/DGPLww3zXlH/?utm_source=ig_web_copy_link'  # Provide a valid Instagram post URL
if not url:
    print("Error: Please provide a valid Instagram post URL.")
else:
    try:
        shortcode = url.split('/')[-2]  # Extract shortcode from URL

        # Fetch the post using the correct method
        post = instaloader.Post.from_shortcode(loader.context, shortcode)

        # Download the post
        loader.download_post(post, target=shortcode)

    except Exception as e:
        print(f"Error downloading post: {e}")
