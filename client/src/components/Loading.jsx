export default function Loading() {
    const colorList = ['#FF4238', '#FFDC00', '#42A2D6', '#9A0006', '#FFF480'];
    
    return (
        <div className="flex items-center justify-center min-h-screen bg-black">
            <div className="flex space-x-2">
                {[...Array(7)].map((_, index) => (
                    <div
                        key={index}
                        className={`h-4 w-4 rounded-full animate-bounce`}
                        style={{ backgroundColor: colorList[index % colorList.length] }}
                    ></div>
                ))}
            </div>
        </div>
    );
}
