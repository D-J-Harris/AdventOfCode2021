use crate::read_file::fileio;

pub fn part_1 () {
    let data: Vec<i32> = fileio::read_file_int(String::from("../inputs/input-01.txt"));
    let ans1 = data.windows(2).filter(|&p| p[0] < p[1]).count();
    println!("solution to day 1 part 1: {}", ans1);
}