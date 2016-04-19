//
//  ViewController.m
//  AssignmentSegue
//
//  Created by Devashish Badlani on 4/15/16.
//  Copyright © 2016 Devashish Badlani. All rights reserved.
//

#import "ViewController.h"
#import "SecondViewController.h"


@interface ViewController ()

@end

@implementation ViewController







- (void)viewDidLoad {
    [super viewDidLoad];
    // Do any additional setup after loading the view, typically from a nib.
    
    
    self.firstTextField.delegate=self;
    
    
    
}

- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

- (IBAction)passTextToVC2Button:(id)sender {
    
    SecondViewController *VC2= [self.storyboard instantiateViewControllerWithIdentifier:@"SecondViewController"];
    VC2.stringFromTextField1=self.firstTextField.text;
    [self presentViewController: VC2 animated:YES completion:nil];
    
    
    
}




-(BOOL) textFieldShouldReturn:(UITextField *)textField
{
    return [textField resignFirstResponder];
}



@end
