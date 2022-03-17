public class Main {
    interface Queue{
        boolean isEmpty();
        boolean isFull();
        void enqueue(int item);
        int dequeue();
        int front();
        int back();
    }

    public class ArrayQueue implements Queue {
        private int front;
        private int back;
        private int queueSize;
        private int[] queueArr;

        public ArrayQueue(int queueSize) {
            this.front = -1;
            this.back = -1;
            this.queueSize = queueSize;
            this.queueArr = new int[this.queueSize];
        }

        @Override
        public boolean isEmpty() {
            if(front == back) {
                front = -1;
                back = -1;
            }
            return front==back;
        }

        @Override
        public boolean isFull() {
            return back == this.queueSize-1;
        }

        @Override
        public void enqueue(int item) {
            if(isFull()) {
                System.out.println("stack is full");
            } else {
                queueArr[++back] = item;
            }
        }

        @Override
        public int dequeue() {
            if(isEmpty()) {
                System.out.println("queue is empty");
            } else {
                System.out.println(queueArr[front+1]);
                front = (front+1) % this.queueSize;
            }
            return queueArr[front];
        }

        @Override
        public int front() {
            return 0;
        }

        @Override
        public int back() {
            return 0;
        }
    }
}
