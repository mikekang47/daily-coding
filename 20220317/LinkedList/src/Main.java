public class Main {
    static class ListNode{
        private String data;
        public ListNode link;

        public ListNode() {
            this.data = null;
            this.link = null;
        }

        public ListNode(String data) {
            this.data = data;
            this.link = null;
        }

        public ListNode(ListNode link) {
            this.data = null;
            this.link = link;
        }

        public ListNode(String data, ListNode link) {
            this.data = data;
            this.link = link;
        }

        public String getData() {
            return this.data;
        }
    }

    public class LinkedList {
        private ListNode head;

        public LinkedList() {
            head = null;
        }

        public void insertNode(ListNode preNode, String data) {
            ListNode newNode = new ListNode(data);

            newNode.link = preNode.link;

            preNode.link = newNode;
        }

        public void insertNode(String data) {
            ListNode newNode = new ListNode(data);
            if(head == null) {
                this.head = newNode;
            } else {
                ListNode tempNode = head;


                while(tempNode.link != null) {
                    tempNode = tempNode.link;
                }

                tempNode.link = newNode;
            }
        }

        public void deleteNode(String data) {
            ListNode preNode = head;
            ListNode tempNode = head.link;

            if(data.equals(preNode.getData())) {
                head = preNode.link;
                preNode.link = null;
            } else {
                while(tempNode != null) {
                    if(data.equals(tempNode.getData())) {
                        if(tempNode.link == null) {
                            preNode.link = null;
                        } else {
                            preNode.link = tempNode.link;
                            tempNode.link = null;
                        }
                        break;
                    } else {
                        preNode = tempNode;
                        tempNode = tempNode.link;
                    }
                }
            }
        }
    }

}
