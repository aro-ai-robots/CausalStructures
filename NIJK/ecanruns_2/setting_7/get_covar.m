function [ covar, iit_val ] = get_covar( X, Y, length, size_m )
%UNTITLED5 Summary of this function goes here
%   Detailed explanation goes here
    pred_cell = populateX(length, X, size_m);
    [b, s, e, c, l] = mvregress(pred_cell, Y);
    [erows, ecols] = size(e);
    E = transpose(e)*e/erows;
    iit_val =  0.5*log2(det(E));
    covar = (2*pi*exp(1))^size_m*det(cov(Y));
    return
end

