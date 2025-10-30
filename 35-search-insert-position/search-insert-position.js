/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
let nums1
let target1

const binarySearch = function(l, r) {
    console.log(l,r)
    const m = parseInt((r + l) / 2)
    console.log(m)
    console.log(nums1[m], target1)
    if(r < l)
        return l
    if(nums1[m] === target1)
        return m
    else if(nums1[m] > target1)
        return binarySearch(l,m - 1)
    else
        return binarySearch(m + 1,r)
}
var searchInsert = function(nums, target) {
    nums1 = nums
    target1 = target
    return binarySearch(0,nums.length - 1)
};