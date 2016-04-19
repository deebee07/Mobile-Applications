//
//  SecondViewController.m
//  AssignmentSegue
//
//  Created by Devashish Badlani on 4/15/16.
//  Copyright © 2016 Devashish Badlani. All rights reserved.
//

#import "SecondViewController.h"

@interface SecondViewController ()

@end

@implementation SecondViewController






- (void)viewDidLoad {
    [super viewDidLoad];
    // Do any additional setup after loading the view.
    
    NSInteger b = [self.stringFromTextField1 integerValue];
    NSString* myNewString = [NSString stringWithFormat:@"%li", b-32];
    
    
    
    
    self.displayLabel2.text=myNewString;
    
    
    
    
    
    
    //
    
}

- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

/*
#pragma mark - Navigation

// In a storyboard-based application, you will often want to do a little preparation before navigation
- (void)prepareForSegue:(UIStoryboardSegue *)segue sender:(id)sender {
    // Get the new view controller using [segue destinationViewController].
    // Pass the selected object to the new view controller.
}
*/

@end
