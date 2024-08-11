class Rectangle {
    private:
        int width, height;
    public:
        Rectangle(int width, int height) {
            this->width = width;
            this->height = height;
        }
        int get_width() const {
            return this->width;
        }
        int get_height() const {
            return this->height;
        }
        void set_width(int width) {
            if (not(0<width and width <= 1000)){return;}
            this->width = width;
        }
        void set_height(int height) {
            if (not(0<height and height <= 2000)){return;}
            this->height = height;
        }
        int area() const {
            return width*height;
        }
        int perimeter() const {
            return (width+height)*2;
        }
        bool is_square() const {
            return width == height;
        }
};
