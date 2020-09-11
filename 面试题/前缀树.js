class Node {
    constructor(left, right) {
        this.left = left;
        this.right = right;
        this.value = null;
    }
}

class SegementTree {
    constructor(nums, fn) {
        this.n = nums.length;
        this.fn = fn;
        this.data = nums;
        this.tree = new Array(this.n * 4);

        this.buildTree(1, 0, this.n - 1);
    }

    buildTree(i, l, r) {
        this.tree[i] = new Node(l, r);
        if (l == r) {
            this.tree[i].value = this.data[l]
            return
        }

        const mid = (l + r) >> 1
        this.buildTree(2 * i, l, mid);
        this.buildTree(2 * i + 1, mid + 1, r);

        this.tree[i].value = this.mergeChildren(i)
    }

    mergeChildren(i) {
        return this.fn(this.tree[2 * i].value, this.tree[2 * i + 1].value)
    }

    update(i, value) {
        this.set(1, i, value);
    }

    set(p, target, value) {
        let cur = this.tree[p]
        if (cur.l == cur.r) {
            cur.value = value
            return
        }

        mid = (cur.left + cur.right) >> 1

        if (p <= mid) {
            this.set(2 * mid, target, value)
        } else {
            this.set(2 * mid + 1, target, value)
        }

        cur.value = this.mergeChildren(p)
    }

    query(targetLeft, targetRight) {
       return this.get(1, targetLeft, targetRight)
    }

    get(p, targetLeft, targetRight) {
        const cur = this.tree[p]
        if (!cur) return;

        if (cur.left === targetLeft && cur.right === targetRight) {
            return cur.value
        }

        const mid = (cur.left + cur.right) >> 1

        if (targetRight <= mid) {
            return this.get(2 * p, targetLeft, targetRight)
        } else if (targetLeft >= mid + 1) {
            return this.get(2 * p + 1, targetLeft, targetRight)
        } else {
            return this.fn(this.get(2 * p, targetLeft, mid), this.get(2 * p + 1, mid + 1, targetRight))
        }

    }

}

function sum(a,b) {
    return a + b
}

const tree = new SegementTree([1, 3, 5], sum)
console.log(tree.query(0, 1), tree.query(1, 2), tree.query(0, 2))

tree.update(1, 10)
console.log(tree.query(0, 1), tree.query(1, 2), tree.query(0, 2))
