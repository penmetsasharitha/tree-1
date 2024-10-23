class Tnode:
    def _init_(self,value):
        self.value=value
        self.left=None
        self.right=None

# root=None
# root.value=Tnode(11)
# root.left=Tnode(5)
# root.left.left=Tnode(7)
# root.left.left.right=Tnode(9)
# root.right=Tnode(3)
# root.right.left=Tnode(6)
# root.right.right=Tnode(8)

    def Create(arr,i,n):
        if i<n:
            Temp=Tnode(arr[i])
            root=Temp
            root.Create(arr,2*i+1,n)
            root.Create(arr,2*i+2,n) 
            return root
        return None
    arr=[11,5,7,9,3,6,8]
    Create(arr,0,len(arr))   # function call

    def Post_order(root):
        if not root :
            return
            Post_order(root.left)
            Post_order(root.right)
        print(root.value,end=" ")
    Post_order(root)  # function call
   
    def Pre_order(root):
        if not root :
            return
            Pre_order(root.left)
            Pre_order(root.right)
        print(root.value,end=" ")
    Pre_order(root)    # function call

    def In_order(root):
        if not root :
            return
            In_order(root.left)
            In_order(root.right) 
        print(root.value,end=" ")
    In_order(root)     # function call