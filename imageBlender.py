import cv2

def blend_images(background_path, overlay_path, output_replace_white_path):
    # Read the background and overlay images
    background = cv2.imread(background_path)
    overlay = cv2.imread(overlay_path)

    # Convert images to the same size
    background = cv2.resize(background, (overlay.shape[1], overlay.shape[0]))

    # Convert the background to grayscale
    gray_background = cv2.cvtColor(background, cv2.COLOR_BGR2GRAY)

    # Threshold the grayscale image to detect white areas
    _, thresholded = cv2.threshold(gray_background, 100, 255, cv2.THRESH_BINARY)

    # Extract the white areas from the overlay image using the threshold
    white_areas = cv2.bitwise_and(overlay, overlay, mask=thresholded)

    # Extract the non-white areas from the background image
    non_white_areas = cv2.bitwise_and(background, background, mask=~thresholded)

    # Combine the white areas from the overlay and non-white areas from the background
    result_replace_white = cv2.add(white_areas, non_white_areas)

    # Save the results to the specified output paths
    cv2.imwrite(output_replace_white_path, result_replace_white)

if __name__ == "__main__":
    # Paths of background, overlay and output images
    background_image_path = "C:/Users/karim/Desktop/VSCode Projects/SelfStudy/ImageBlender/cocacola.png"
    overlay_image_path = "C:/Users/karim/Desktop/VSCode Projects/SelfStudy/ImageBlender/pattern.jpg"
    output_replace_white_path = "C:/Users/karim/Desktop/pattern_in_white.png"

    # Calling the blend_images function
    blend_images(background_image_path, overlay_image_path, output_replace_white_path)

